import fire
from . import auth

fire.Fire({
    'register': auth.register,
    'login': auth.login,
    'verify': auth.verify_token,
    'refresh': auth.refresh_token,
})
