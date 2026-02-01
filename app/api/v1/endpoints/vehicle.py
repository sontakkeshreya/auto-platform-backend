from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class VinDecodeRequest(BaseModel):
    vin: str

class VinDecodeResponse(BaseModel):
    make: str
    model: str
    year: int
    engine: str
    trim: str
    transmission: str

@router.post("/decode-vin", response_model=VinDecodeResponse)
def decode_vin(payload: VinDecodeRequest):
    # STUB: hardcoded for now
    return VinDecodeResponse(
        make="Maruti Suzuki",
        model="Swift",
        year=2022,
        engine="1.2L Petrol",
        trim="ZXI",
        transmission="Manual"
    )
