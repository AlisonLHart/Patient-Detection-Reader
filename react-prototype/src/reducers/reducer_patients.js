import {SET_PATIENTS} from '../constants';

export default (state = [], action) => {
    switch(action.type){
        case SET_PATIENTS:
            const {patients} = action;
            return patients
    default:
        return state;
    }
}