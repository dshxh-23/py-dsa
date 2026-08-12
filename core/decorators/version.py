class VersionRegistry:
    """
    Global registry mapping algorithm names to their versioned implementations.
    Never instantiated; all state lives on the class itself.
    """

    _registry = {}


    # -- -- private methods -- --


    @classmethod
    def _register(cls, func):
        """
        Called by @versioned at import time.
        Inserts func into the registry and enforce all invariants.
        """

        name = getattr(func, "version_name", None)
        version = getattr(func, "version_number", None)

        if name not in cls._registry:
            cls._registry[name] = []

        bucket = cls._registry[name]

        # Invariant 1: version numbers must be unique within a name
        for existing in bucket:
            if existing.version_number == version:
                raise ValueError(
                    f"[VersionRegistry] {name} already has a version {version}."
                )

        # Invariant 2: at most one default per name
        if func.is_default:
            for existing in bucket:
                if existing.is_default:
                    raise ValueError(
                        f"[VersionRegistry] {name} already has a default version, version {version}"
                    )

        bucket.append(func)
        bucket.sort(key=lambda f: f.version_number)


        # -- -- public methods -- --


    @classmethod
    def get(cls, name, version):
        """Return the function registered for the requested version."""

        cls._verify_name(name)

        for func in cls._registry[name]:
            if func.version_number == version:
                return func

        available = [f.version_number for f in cls._registry[name]]
        raise KeyError(
            f"[VersionRegistry] {name} has no version {version}. Available versions: {available}"
        )

    @classmethod
    def get_default(cls, name):
        """Return the default implementation for the given name."""

        cls._verify_name(name)

        bucket = cls._registry[name]

        # returning default version
        for func in bucket:
            if func.is_default:
                return func

        # fallback: highest version number
        return bucket[-1]   # bucket is sorted in ascending order


    @classmethod
    def list_versions(cls, name):
        """Return a list of metadata dictionaries for the registered versions."""

        # return empty list if no version exists
        if name not in cls._registry:
            return []

        result = []
        for func in cls._registry[name]:
            complexity = getattr(func, "_complexity", None)
            result.append(
                {
                    "version": func.version_number,
                    "default": func.is_default,
                    "note": func.version_note,
                    "function": func,
                    "time": getattr(complexity, "time", None),
                    "space": getattr(complexity, "space", None),
                    "complexity_note": getattr(complexity, "note", None),
                }
            )
        return result


    # -- -- helper methods -- --


    @classmethod
    def _verify_name(cls, name):
        if name not in cls._registry:
            raise ValueError(
                f"[VersionRegistry] No algorithm named '{name}' is registered. "
                f"Available names: {list(cls._registry.keys())}"
            )
        return True
        

# ---- ---- decorator ---- ----


def version(name: str, version: int, default: bool = False, note: str = ""):
    """
    Attach version metadata to a function and register it in VersionRegistry.

    Args:
        name (str): algorithm family this version belongs to
        version (int): version number for this implementation
        default (bool): whether this is the default implementation
        note (str): descriptive note for the version
    """

    if not isinstance(version, int) or version < 1:
        raise ValueError(
            f"[VERSIONED] 'version' must be a positive integer, got {version!r}"
        )

    # type check for name
    if not isinstance(name, str) or not name.strip():
        raise ValueError(
            f"[VERSIONED] 'name' must be a non-empty string, got {name!r}"
        )

    def decorator(func):

        # add version metadata to func object
        func.version_name = name
        func.version_number = version
        func.is_default = default
        func.version_note = note

        # add function to registry
        VersionRegistry._register(func)

        # return unchanged function
        return func

    return decorator
