import React from "react";
import { Container, ProgressBar } from "react-bootstrap";

const Scan = ({ item, variant }) => {
  const now =
    variant === "info"
      ? Math.floor((item["files"]["completed"] / item["files"]["total"]) * 100)
      : 100;
  return (
    <Container className="scan d-flex text-muted px-4 py-2">
      <div className="d-flex flex-basis">
        <div
          className={`circle d-flex align-items-center justify-content-center rounded-circle bg-${variant} mt-1 me-3`}
        >
          Icon
        </div>
        <div className="w-100">
          <p>ID: Scan</p>
          <ProgressBar
            id={item._id}
            className="w-100 mt-0 h-25"
            variant={variant}
            now={now}
            label={`${now}%`}
          />
        </div>
      </div>
      <p>{item.size}</p>
      <p>{item.files.total}</p>
      <p>{item.submiTime.date}</p>
    </Container>
  );
};
export default Scan;
