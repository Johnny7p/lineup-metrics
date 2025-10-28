from fastapi import FastAPI
app = FastAPI()
@app.get('/now')
def now(cam: str='cam_example'):
    # TODO: load recent summary and return tiles
    return {'ok': True, 'cam': cam}
