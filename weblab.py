# Check the starting point: GET https://c20240327a.challenges.weblab.technology/a.
# Analyze and interpret. Provide the solution of how to get to the `x`, if feasible.
# Aim to minimize networking operations.

# So, we don't know, how many nesting we can have. 
# But, analyzeid responses from server, we can assume, 
# that parameter always the one latin symbol.
# If parameter is only one symbol, we need to take latin alphabet, 
# and to send async request. 
# So we get all results and we check where we can find symbol "x".

import httpx
import asyncio

accept = "x"
az = ("a b c d e", "f g h i j", "k l m n o", "p q r s t", "u v w x y z")
url_api = f"https://c20240327a.challenges.weblab.technology"

async def test_result(search: list) -> bool:
    for i in search:
        if i == accept:
            return True

    return False

async def fetch_url(client: httpx.AsyncClient, param: str) -> dict:
    url = f"{url_api}/{param}"
    response = await client.get(url)
    res = {
        param: response.text
    }
    return res

async def main() -> list:
    results = list()

    for param_search in az:
        await asyncio.sleep(2)
        data = param_search.split(" ")
        async with httpx.AsyncClient() as client:
            tasks = [fetch_url(client, param) for param in data]
            responses = await asyncio.gather(*tasks)

        for response in responses:
            for key, value in response.items():
                accept = await test_result(value.split(" "))
                if accept is True:
                  results.append(key)

    print(results)
    return results


if __name__ == "__main__":
    asyncio.run(main())
