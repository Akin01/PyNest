from config import config
from nest.core.app import App
from src.user.user_module import UserModule
from src.product.product_module import ProductModule
from src.example.example_module import ExampleModule

app = App(
    description="PyNest service", modules=[UserModule, ProductModule, ExampleModule]
)


@app.on_event("startup")
async def startup():
    await config.create_all()
