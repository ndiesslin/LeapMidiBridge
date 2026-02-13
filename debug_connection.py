import socket
import asyncio
import websockets

async def test_connection(uri):
    print(f"Testing {uri}...", end=" ")
    try:
        # Use asyncio.wait_for for the timeout instead
        async with websockets.connect(uri) as ws:
            print("SUCCESS!")
            return True
    except Exception as e:
        print(f"FAILED: {e}")
        return False

async def main():
    print("--- Python Network Debug ---")
    
    # Check if the port is open at the socket level
    for host in ['127.0.0.1', '::1']:
        s = socket.socket(socket.AF_INET if host == '127.0.0.1' else socket.AF_INET6, socket.SOCK_STREAM)
        try:
            s.connect((host, 6437))
            print(f"Socket level {host}:6437: OPEN")
        except:
            print(f"Socket level {host}:6437: CLOSED")
        finally:
            s.close()

    uris = [
        "ws://127.0.0.1:6437/v6.json",
        "ws://localhost:6437/v6.json",
        "ws://[::1]:6437/v6.json",
    ]

    for uri in uris:
        try:
            await asyncio.wait_for(test_connection(uri), timeout=2.0)
        except asyncio.TimeoutError:
            print(f"Testing {uri}... TIMEOUT")

if __name__ == "__main__":
    asyncio.run(main())
