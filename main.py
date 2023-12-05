import fastapi
import uvicorn
import fastapi_chameleon
from views import home, account, packages

app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app)


def configure():
    configure_templates()
    configure_routers()


def configure_templates():
    fastapi_chameleon.global_init("templates")


def configure_routers():
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == "__main__":
    main()
else:
    configure()
