import { combineReducers } from 'redux';
import TimetableReducer from './reducer_timetable';

const rootReducer = combineReducers({
  timetable: TimetableReducer
});

export default rootReducer;
