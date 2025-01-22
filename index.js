import express from  "express";
const app = express ();
const port = 5000;
 
app.get("/",(req,res)=>{
    res.send("hellkcbdjbo baby");
});

app.get("/me",(req,res)=>{
    res.send("helldsfeaffkcbdjbo baby");
});


app.listen(port ,()=>{
    console.log(`server staterd int the port ${port}`);
});