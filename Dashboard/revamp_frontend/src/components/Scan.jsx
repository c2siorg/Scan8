import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faArrowsRotate,
  faCheck,
  faExclamation,
  faPause,
} from "@fortawesome/free-solid-svg-icons";
import { Container, ProgressBar } from "react-bootstrap";

const timeAgo = (input) => {
  const date = (input instanceof Date) ? input : new Date(input);
  const formatter = new Intl.RelativeTimeFormat('en');
  const ranges = {
    years: 3600 * 24 * 365,
    months: 3600 * 24 * 30,
    weeks: 3600 * 24 * 7,
    days: 3600 * 24,
    hours: 3600,
    minutes: 60,
    seconds: 1
  };
  const secondsElapsed = (date.getTime() - Date.now()) / 1000;
  for (let key in ranges) {
    if (ranges[key] < Math.abs(secondsElapsed)) {
      const delta = secondsElapsed / ranges[key];
      return formatter.format(Math.round(delta), key);
    }
  }
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
        <p>ID: Scan {item._id} </p>
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
