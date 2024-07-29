from fastapi import APIRouter, HTTPException, File, UploadFile

from models.certidoes import Certidoes
from utils.file_utils import save_file_data, read_file_data
from utils.s3_utils import upload_file_to_s3

router = APIRouter()


@router.post("/upload", response_model=Certidoes)
async def upload_certidoes(file: UploadFile = File(...)):
    file_url = upload_file_to_s3(file.file, file.filename)

    if file_url is None:
        raise HTTPException(status_code=500, detail="Falha ao enviar o arquivo")

    save_file_data(file.filename, file_url)
    return {"filename": file.filename, "url": file_url}


@router.get("/certidoes", response_model=list[Certidoes])
async def get_certidoes():
    return read_file_data()
