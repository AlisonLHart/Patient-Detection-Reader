import { combineReducers} from 'redux';
import user from './reducer_user';
import patients from './reducer_patients';

export default combineReducers({
    user,
    patients
})