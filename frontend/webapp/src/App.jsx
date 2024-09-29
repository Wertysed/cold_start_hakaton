import { useEffect, useState } from "react"
import { Provider, LikeButton } from "@lyket/react";
import img from "./hat.png"
import "./styles/main.css"
import {v4 as uuidv4} from 'uuid';




function App() {                                                           
  let images = [
    {
      name: "Video0",
      id: "909"
    },
    {
      name: "Video0",
      id: "513515"
    },
    {
      name: "Video0",
      id: "3"
    },
    {
      name: "Video0",
      id: "4"
    },
    {
      name: "Video0",
      id: "3123"
    },
    {
      name: "Video0",
      id: "5235"
    },
    {
      name: "Video0",
      id: "32"
    },
    {
      name: "Video0",
      id: "4353"
    },
    {
      name: "Video0",
      id: "325"
    },
    {
      name: "Video0",
      id: "22"
    },
  ]
  const [state, setState] = useState(1);

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
        "mark" : 1
      })
    })
    const requestWithRates = {
      "cookies" : {
        "session_id" : localStorage.getItem("userId")
      },
      "checked_video" : sendLikesDises
    }
    console.log(requestWithRates)
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
    console.log("Dislicked Vieos: " + dislikedVideos)
    console.log("licked Vieos: " + likedVideos)
  }

  useEffect(() => {
    if (localStorage.getItem("userId") === null) {
      localStorage.setItem("userId", uuidv4())
    }
    else {
      console.log("LOgged bu ID")
    }
    let request = {
      "cookies" : {
        "session_id": localStorage.getItem("userId")
      },
      "checked_video" : [
        {
          "video_id": "",
          "mark" : "",
        }
      ]
    }
    console.log(request)
  })
    return (
      <div className="App">
        <img draggable="false" className="hat" src={img}></img>
        <div className="header">
          <a name="pageStart"></a>
          <h1 style={{marginBottom: "40px", marginTop: "5%"}}>Ваши рекомендации:</h1>
          <hr style={{width: "95%", height: "3px", backgroundColor: "white", borderRadius: "40px"}}></hr>
        </div>
        {images.map((videoData, key) =>{ 
          return(
          <div className="video" sty  le={{textAlign: "center"}}>
            <h style={{textAlign: "start"}}>{videoData.name}</h> 
            <p style={{textAlign: "start", marginBottom: "20px"}}>Описание выпыпвыпып выпып выпып выпып выпып выпып выпып выпып выпып выпып выпып</p>
            
            <p style = {{marginRight: "30px", display: "inline"}}>
              <input type="checkbox" class="demoCustomCheckbox" id={key} onClick={() => rated(videoData.id, key, "like")}/>
              <label style={{width: "10px", display: "inline"}} for={key}> </label>
            </p>
            <p style = {{display: "inline"}}>
              <input type="checkbox" class="demoCustomCheckboxDis" id={key + "dis"} onClick={() => rated(videoData.id, key, "dislike")}/>
              <label style={{width: "10px", display: "inline"}} for={key + "dis"}> </label>
          </p>
          </div>
        )})}
        <div style={{width: "100%", float: "left", textAlign: "center"}}>
          <a href="#pageStart"><button className="button" onClick={() => refreshVideos(likedVideos, dislikedVideos)}>Обновить</button></a>
        </div>
    </div>
    );
  }

export default App;
