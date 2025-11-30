import axios from "axios";
export const getPosts = async () => {
    try {
        const res = await axios.get("http://127.0.0.1:8000/api/posts", { timeout: 5000 });
        console.log(res.data);
        return res.data;
    } catch (err) {
        //console.error("GET / failed:", err?.response?.status, err?.message);
        // қате бойынша өңдеу: 404 болса бос массив, басқаша болса null немесе throw
        if (err?.response?.status === 404) return [];
        return 404;
    }
};