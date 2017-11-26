import React from 'react';

function renderButton(service) {
  if (service.trainID) {
    return (
      <button className="btn btn-warning btn-xs">Done</button>
    );
  } else {
    return ('');
  }
}

const TimetableItem = (props) => {
  const service = props.service;
  const stl = {
    backgroundColor: service.color
  };

  return (
    <div className="timetable-item" style={stl}>
      <h5>{service.trainID ? `Train: ${service.trainID}` : ''}</h5>
      <h6>{service.date ? `Date: ${service.date}` : ''}</h6>
      <h6><b>{service.exam ? `Exam: ${service.exam}` : ''}</b></h6>
      {renderButton(service)}
    </div>
  );
}

export default TimetableItem;