import { Modal, Button } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUpload } from "@fortawesome/free-solid-svg-icons";
import { useRef, useState } from "react";

const UploadModal = ({ modal, setModal }) => {
  const inputRef = useRef(null);
  const [upload, setUpload] = useState(true);
  const [msg, setMsg] = useState("");
  function handleSubmit(event) {
    event.preventDefault();
    const selectedFiles = inputRef.current.files;
    const formData = new FormData();
    for (let i = 0; i < selectedFiles.length; i++) {
      formData.append("dir", selectedFiles[i]);
    }
    
    const requestOptions = {
      method: "POST",
      body: formData,
    };
    fetch(`${process.env.REACT_APP_FLASK_URL}/upload`, requestOptions)
      .then((response) => {
        //console.log(response);
        setModal(false);
        setMsg("");
      })
      .catch((err) => console.error(err));
  }

  function update() {
    let numFiles = inputRef.current?.files?.length;
    
    if (numFiles > 0) {
      setUpload(false);
      setMsg(`${numFiles} files uploaded`);
    } else {
      setUpload(true);
    }
  }
  return (
    <Modal
      backdrop="static"
      centered
      show={modal}
      onHide={() => setModal(false)}
    >
      <form encType="multipart/form-data" onSubmit={handleSubmit}>
        <div className="file-upload">
          <h4>Upload Files</h4>
          <input
            type="file"
            webkitdirectory=""
            mozdirectory=""
            id="customFile"
            ref={inputRef}
            onChange={update}
            style={{ display: "none" }}
          />
          <label htmlFor="customFile" className="custom-upload">
            <FontAwesomeIcon
              icon={faUpload}
              size={"2xl"}
              style={{ color: "#478cfb" }}
            />
            <p>Click to browse files</p>
          </label>
          <p> {msg} </p>
        </div>
        <div className="col-sm d-flex justify-content-between mx-4 mb-2">
          <Button
            className="px-4"
            variant="danger"
            onClick={() => {
              setMsg("");
              setModal(false);
            }}
          >
            Cancel
          </Button>
          <Button
            className="px-4"
            variant="success"
            type="submit"
            value="Upload"
            disabled={upload}
          >
            Upload
          </Button>
        </div>
      </form>
    </Modal>
  );
};
export default UploadModal;
