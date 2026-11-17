import argparse
import asyncio
from pathlib import Path

if __package__:
    from .honeypot import serve_host
else:
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from dynahive.honeypot import serve_host


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", default=str(Path(__file__).resolve().parent))
    parser.add_argument("--deployment", required=True)
    parser.add_argument("--bind", default="0.0.0.0")
    parser.add_argument("--gateway-port", type=int, default=18080)
    args = parser.parse_args()
    asyncio.run(serve_host(Path(args.project_root), args.deployment, args.bind, args.gateway_port))


if __name__ == "__main__": main()
