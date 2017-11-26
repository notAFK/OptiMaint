import React, { Component } from 'react';
import { connect } from 'react-redux';
import Title from '../components/title';

class Timetable extends Component {

  render() {
    console.log(this.props.timetable);
    return (
      <div className="container">
        <Title />
        <table className="timetable">
          <thead className="timetable-header">
            <tr>
              <th>Trains</th>
              <th>Monday</th>
              <th>Tuesday</th>
              <th>Wednesday</th>
              <th>Thursday</th>
              <th>Friday</th>
              <th>Saturday</th>
              <th>Sunday</th>
            </tr>
          </thead>
          <tbody className="timetable-body">
          </tbody>
        </table>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return { timetable: state.timetable };
}

export default connect(mapStateToProps)(Timetable);