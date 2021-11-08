from fastapi import FastAPI
from pydantic import BaseModel
from jax_unirep import get_reps

class Sequence(BaseModel):
    protein: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/unirep")
def unirep(seq: Sequence):
    try:
        protein_seq = str(seq.protein).replace("*", '').replace(' ','')
        h_avg, h_final, c_final = get_reps(protein_seq)
        embedding = h_avg.tolist()
        return {"unirep": embedding[0]}
    except Exception as e:
        print(e)
        return {'error', str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)