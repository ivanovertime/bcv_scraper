import os
import multiprocessing
import uvicorn


def _get_workers() -> int:
    try:
        return int(os.getenv("WORKERS", ""))
    except ValueError:
        pass

    cores = multiprocessing.cpu_count()
    return (cores * 2) + 1


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    reload = os.getenv("RELOAD", "false").lower() in {"1", "true", "yes"}
    log_level = os.getenv("LOG_LEVEL", "info")

    uvicorn.run(
        "main:app",
        host=host,
        port=port,
        reload=reload,
        workers=_get_workers(),
        log_level=log_level,
    )
