import { useEffect, useState } from "react"
import { Provider, LikeButton } from "@lyket/react";
import axios, { Axios } from "axios"
import img from "./hat.png"
import "./styles/main.css"
import {v4 as uuidv4} from 'uuid';




function App() {                                                           

  const [state, setState] = useState(1);
  const [data, setData] = useState([]);
  const images = [
    {
      "id": "fdsfs",
      "name": "fdsaf"
    }
  ]

  const refreshVideos = (likes, dislikes) => {
    let sendLikesDises = []
    likes.map((videoId) => {
      sendLikesDises.push({
        "video_id" : videoId,
        "mark" : 1
      })
    })
    dislikes.map((videoId) => {
      sendLikesDises.push({
        "video_id" : videoId,
        "mark" : 0
      })
    })
    const requestWithRates = {
      "cookies" : {
        "session_id" : localStorage.getItem("userId")
      },
      "checked_video" : sendLikesDises
    }
    console.log(requestWithRates)
    axios.post("http://89.111.170.10:9999/get_video", requestWithRates)
    .then(response => {setData(response.data);
      for (let i = 0; i < 10; i++){
        document.getElementById(i).checked = false
        document.getElementById(i + "dis").checked = false
      }
    }
      )
  }

  let likedVideos = []
  let dislikedVideos = []

  const rated =  (videodat, uncheck, rate) => {
    if (rate === "like") {
      if (likedVideos.indexOf(String(videodat)) === -1) {
        likedVideos.push(videodat)
          if (document.getElementById(uncheck + "dis").checked === true) {
            document.getElementById(uncheck + "dis").checked = false;
            let toDelete = dislikedVideos.indexOf(videodat)
            dislikedVideos.splice(toDelete, 1)
          }
      }
      else {
        let toDelete = likedVideos.indexOf(videodat)
        if (toDelete !== -1) {
          likedVideos.splice(toDelete, 1);
        }
      }}
    else {
      if (dislikedVideos.indexOf(String(videodat)) === -1) {
        dislikedVideos.push(videodat)
        if (document.getElementById(uncheck).checked === true) {
          document.getElementById(uncheck).checked = false;
          let toDelete = likedVideos.indexOf(videodat)
          likedVideos.splice(toDelete, 1)
        }
      }
      else {
        let toDelete = dislikedVideos.indexOf(videodat)
        
        if (toDelete !== -1) {
          dislikedVideos.splice(toDelete, 1);
        }
      }
    }
    let checkedVideos = []
    dislikedVideos.map((videoData) => {
      checkedVideos.push({
        "video_id": videoData,
        "mark": 0,
      })
    })
    likedVideos.map((videoData) => {
      checkedVideos.push({
        "video_id": videoData,
        "mark": 1,
      })
    })
    console.log(checkedVideos)
    let req = 
    {
      "cookies": {
        "session_id": localStorage.getItem("userId")
      },
      "checked_video": checkedVideos
    }
  }

  useEffect(() => {
    if (localStorage.getItem("userId") === null) {
      localStorage.setItem("userId", uuidv4())
    }
    else {
      console.log("LOgged bu ID")
    }
    
    let req = 
    {
      "cookies": {
        "session_id": localStorage.getItem("userId")
      },
      "checked_video": [
      ]
    }


    axios.post("http://89.111.170.10:9999/get_video", req)
    .then(response => {setData(response.data)}
      )
    .catch(error => console.error(error));
  }, []);

    return (
      <div className="App">
        <img draggable="false" className="hat" src={img}></img>
        <div className="header">
          <a name="pageStart"></a>
          <h1 style={{marginBottom: "40px", marginTop: "5%"}}>Ваши рекомендации:</h1>
          <hr style={{width: "95%", height: "3px", backgroundColor: "white", borderRadius: "40px"}}></hr>
        </div>
        {data.map((videoData, key) =>{ 
          console.log(videoData.video_id)
          return(
          <div className="video" style={{display: "inline-flex"}}>
              
              <div style={{display: "inline-block"}}>
                  <h style={{textAlign: "start"}}>{videoData.title}</h> 
                  <p style={{textAlign: "start", marginBottom: "20px", fontSize: "10pt", color: "gray", marginTop: "7px", overflow: "auto", maxHeight: "150px", marginBottom: "10px"}}>{videoData.description}</p>

                <div style={{display: "inline-flex"}}>
                  <p style = {{marginRight: "30px"}}>
                    <input type="checkbox" class="demoCustomCheckbox" id={key} onClick={() => rated(videoData.video_id, key, "like")}/>
                    <label style={{width: "10px", clear: "both"}} for={key}> </label>
                  </p>
                  <p style = {{clear: "both"}}>
                    <input type="checkbox" class="demoCustomCheckboxDis" id={key + "dis"} onClick={() => rated(videoData.video_id, key, "dislike")}/>
                    <label style={{width: "10px"}} for={key + "dis"}> </label>
                  </p>
                  </div>
                </div>
            
          </div>
        )})}
        <div style={{width: "100%", float: "left", textAlign: "center"}}>
          <a href="#pageStart"><button className="button" onClick={() => refreshVideos(likedVideos, dislikedVideos)}>Обновить</button></a>
        </div>
    </div>
    );
  }

export default App;
