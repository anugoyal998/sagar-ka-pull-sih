import axios from "axios"

async function upload(file){
    const formData = new FormData();
    formData.append("file", file);
    formData.append("upload_preset", "mechat");
    const url = `https://api.cloudinary.com/v1_1/${
    import.meta.env.VITE_CLOUD_NAME
    }/image/upload`;
    const { data } = await axios.post(url, formData);
    return data?.secure_url
}