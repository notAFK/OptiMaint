import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import reduxPromise from 'redux-promise';

import reducers from './reducers';
import Timetable from './containers/timetable';

const createStoreWithMiddleware = applyMiddleware(reduxPromise)(createStore);

ReactDOM.render(
  <Provider store={createStoreWithMiddleware(reducers)}>
    <BrowserRouter>
      <Switch>
        <Route path="/" component={Timetable} />
      </Switch>
    </BrowserRouter>
  </Provider>
  , document.querySelector('.container'));
