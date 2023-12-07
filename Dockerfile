# Gunakan image Python versi 3.11 sebagai dasar
FROM python:3.11-alpine3.18

# Set direktori kerja di dalam container
WORKDIR /app

# Salin requirements.txt terlebih dahulu
COPY requirements.txt .

# Install dependensi Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Salin seluruh kode sumber aplikasi
COPY . .

# Port yang akan diexpose oleh aplikasi
EXPOSE 8001

# Perintah untuk menjalankan aplikasi menggunakan uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
