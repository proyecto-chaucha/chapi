from fastapi import FastAPI
from aiorpcx import timeout_after, connect_rs
from aiohttp import BasicAuth, ClientSession
import aiohttp, json

app = FastAPI()

@app.get("/balance/{address}")
async def read_root(address: str):
	req = {'limit': 2, 'items': [address]}
	resp = None

	async with timeout_after(10):
		async with connect_rs(
			'localhost',
			8000
		) as session:
			session.transport._framer.max_size = 0
			session.sent_request_timeout = 10
			resp = await session.send_request("query", req)
	
	return resp


@app.get("/block/{block_index}")
async def read_root(block_index: int):
	resp = None

	async with ClientSession() as session:
		async with session.post(
			'http://127.0.0.1:20009',
			auth=BasicAuth('chaucha', 'chaucha'),
			json={
			"jsonrpc": "2.0",
			"id": "1e8",
			"method": "getblockhash",
			"params": [block_index]
		}) as response:
			resp = await response.json()
	
	return resp


