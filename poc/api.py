import inspect
import requests

from fastapi import Depends
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials


ROOT_URL = "https://ipv64.net/api.php"
auth = HTTPBearer()


api = FastAPI(
    title="IPv64.net OpenAPI Specification (proof of concept)",
    version="v1",
    description="See [https://ipv64.net](https://ipv64.net) for more information."
)


def current_function_name():
    return inspect.currentframe().f_back.f_code.co_name


def call_ipv64_api(method: str, token: str, endpoint: str="", **kwargs: dict):
    kwargs = kwargs | {
        "headers": {
            "Authorization": f"Bearer {token}"
        }
    }

    response = requests.request(method, f"{ROOT_URL}/{endpoint}", **kwargs)
    return response.json()


@api.get("/get_account_info")
def get_account_info(token: HTTPAuthorizationCredentials = Depends(auth)):
    return call_ipv64_api("get", token.credentials, f"?{current_function_name()}")


@api.get("/get_logs")
def get_logs(token: HTTPAuthorizationCredentials = Depends(auth)):
    return call_ipv64_api("get", token.credentials, f"?{current_function_name()}")

@api.get("/get_domains")
def get_domains(token: HTTPAuthorizationCredentials = Depends(auth)):
    return call_ipv64_api("get", token.credentials, f"?{current_function_name()}")


@api.post("/add_domain")
def add_domain(
    domain: str,
    token: HTTPAuthorizationCredentials = Depends(auth)
):
    return call_ipv64_api("post", token.credentials, data={
        "add_domain": domain
    })


@api.delete("/del_domain")
def del_domain(
    domain: str,
    token: HTTPAuthorizationCredentials = Depends(auth)
):
    return call_ipv64_api("delete", token.credentials, data={
        "del_domain": domain
    })


@api.post("/add_record")
def add_record(
    domain: str,
    prefix: str,
    prefix_type: str,
    content: str,
    token: HTTPAuthorizationCredentials = Depends(auth)
):
    return call_ipv64_api("post", token.credentials, data={
        "add_record": domain,
        "praefix": prefix,
        "type": prefix_type,
        "content": content
    })


@api.delete("/del_record")
def del_record(
    domain: str,
    prefix: str,
    prefix_type: str,
    content: str,
    token: HTTPAuthorizationCredentials = Depends(auth)
):
    return call_ipv64_api("delete", token.credentials, data={
        "del_record": domain,
        "praefix": prefix,
        "type": prefix_type,
        "content": content
    })
