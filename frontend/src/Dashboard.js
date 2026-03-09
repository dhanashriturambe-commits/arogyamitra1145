import axios from "axios"

function Dashboard(){

const getWorkout=async()=>{

const res=await axios.get("http://localhost:8000/workout")

console.log(res.data)

}

return(

<div>

<button onClick={getWorkout}>
Generate Workout Plan
</button>

</div>

)

}

export default Dashboard