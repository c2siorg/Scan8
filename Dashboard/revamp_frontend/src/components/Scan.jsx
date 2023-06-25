import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faArrowsRotate,
  faCheck,
  faExclamation,
  faPause,
} from "@fortawesome/free-solid-svg-icons";
import { Container, ProgressBar } from "react-bootstrap";

const timeAgo = (date) => {
  const seconds = Math.floor((new Date() - date) / 1000);

  let interval = Math.floor(seconds / 31536000);
  if (interval > 1) {
    return interval + " years ago";
  }

  interval = Math.floor(seconds / 2592000);
  if (interval > 1) {
    return interval + " months ago";
  }

  interval = Math.floor(seconds / 86400);
  if (interval > 1) {
    return interval + " days ago";
  }

  interval = Math.floor(seconds / 3600);
  if (interval > 1) {
    return interval + " hours ago";
  }

  interval = Math.floor(seconds / 60);
  if (interval > 1) {
    return interval + " minutes ago";
  }

  if (seconds < 10) return "just now";

  return Math.floor(seconds) + " seconds ago";
};

const Icon = ({ status }) => {
  switch (status) {
    case "warning":
      return <FontAwesomeIcon icon={faPause} style={{ color: "#ffffff" }} />;
    case "info":
      return <FontAwesomeIcon icon={faArrowsRotate} style={{ color: "#ffffff" }} />;
    case "success":
      return <FontAwesomeIcon icon={faCheck} style={{ color: "#ffffff" }} />;
    case "danger":
      return <FontAwesomeIcon icon={faExclamation} style={{ color: "#ffffff" }} />;
    default:
      return null;
  }
};

const Scan = ({ item, variant }) => {
  const date = timeAgo(
    new Date(
      item.submitTime.date.split("-").reverse().join("-") +
        " " +
        item.submitTime.time
    )
  );
  const now =
    variant === "info"
      ? Math.floor((item["files"]["completed"] / item["files"]["total"]) * 100)
      : 100;
  return (
    <Container className="scan d-flex text-muted px-4 py-2">
      <div
        className={`circle d-flex align-items-center justify-content-center rounded-circle bg-${variant} mt-1 me-3`}
      >
        <Icon status={variant} />
      </div>

      <div className="scan-progress">
        <p>ID: Scan</p>
        <ProgressBar
          id={item._id}
          className="w-100 mt-0 h-25"
          variant={variant}
          now={now}
          label={`${now}%`}
        />
      </div>
      <div className="scan-details">
        <p>{item.size}</p>
        <p>{item.files.total}</p>
        <p>{date}</p>
      </div>
    </Container>
  );
};
export default Scan;
