import React, { Component } from 'react';
import { connect } from 'react-redux';
import Title from '../components/title';
import _ from 'lodash';
import TimetableItem from '../components/timetable_item';

class Timetable extends Component {

  renderColumn(data) {
    return data.map((d) => {
      return (
        <td key={d.trainID}><TimetableItem service={d} /></td>
      );
    });
  }

  renderRows(data) {
    return data.map((d) => {
      return (
        <tr>{d}</tr>
      );
    });
  }


  render() {
    var data = this.props.timetable;
    for(var i=0;i<data.length;i++) {
      while(data[i].length != 7) {
        data[i].push({});
      }
    }
    const data1 = data.map((d) => this.renderColumn(d));
    const tbl = this.renderRows(data1);

    return (
      <div className="container">
        <Title />
        <table className="timetable">
          <thead className="timetable-header">
            <tr>
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
            {tbl}
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