import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import NavBar from "./components/Navbar";
import io from "socket.io-client";
import Scan from "./components/Scan";
import UploadModal from "./components/UploadModal";

function App() {
  const flaskUrl = process.env.REACT_APP_FLASK_URL;
  const [data, setData] = useState({ queued: [], running: [], completed: [] });
  const [modal, setModal] = useState(false);
 
  useEffect(() => {
    const socket = io(flaskUrl);
    // Set up listener for events from Flask-SocketIO server
    socket.on("connect", () => console.log("Connected"));
    socket.on("update", (res) => {
      //console.log(res);
      setData((prevData) => ({        
        queued:
          res?.queued 
            ? res.queued
            : prevData.queued,
        running:
          res?.running && res?.queued 
            ? [...prevData.running, ...res.running]
            : res.running,
        completed:
          res?.completed
            ? [...prevData.completed, ...res.completed]
            : prevData.completed,
      }));
    });

    return () => {
      socket.disconnect();
    };
  }, []);

  return (
    <div>
      <NavBar modal={modal} setModal={setModal} />
      <Container className="d-flex text-muted mt-3">
        <p className="scan-header">Scan</p>
        <div className="d-flex justify-content-between">
          <p>Size</p>
          <p>Number of Files</p>
          <p>Submitted</p>
        </div>
      </Container>
      {/* {data ? JSON.stringify(data) : "Data"} */}
      <Container className="bg-white mx-auto p-0">
        <h4>Queued Scans</h4>
        {data.queued.length > 0 &&
          data.queued.map((item) => <Scan item={item} variant={"warning"} />)}
        <h4>Running Scans</h4>
        {data.running.length > 0 &&
          data.running.map((item) => <Scan item={item} variant={"info"} />)}
        <h4>Completed Scans</h4>
        {data.completed.length > 0 &&
          data.completed.map((item) => (
            <Scan item={item} variant={"success"} />
          ))}
      </Container>
      <UploadModal modal={modal} setModal={setModal} />
    </div>
  );
}

export default App;
