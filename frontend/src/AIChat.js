import {useState} from "react"
import axios from "axios"

function AIChat(){

const[msg,setMsg]=useState("")
const[reply,setReply]=useState("")

const sendMessage=async()=>{

const res=await axios.post("http://localhost:8000/ai",{message:msg})

setReply(res.data.response)

}

return(

<div>

<input onChange={(e)=>setMsg(e.target.value)} />

<button onClick={sendMessage}>
Ask AROMI
</button>

<p>{reply}</p>

</div>

)

}

export default AIChat