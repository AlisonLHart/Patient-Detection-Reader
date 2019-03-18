import {SIGNED_IN, SET_PATIENTS} from '../constants';

export function logUser(email) {
    const action = {
        type: SIGNED_IN,
        email
    }
    return action;
}

export function setPatients(patients){
    const action = {
        type: SET_PATIENTS,
        patients
    }
    return action;
}