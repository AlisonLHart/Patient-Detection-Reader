import * as firebase from 'firebase';

const config = {
    apiKey: "AIzaSyBcljcQC1PeMEEGgwdePfO-S0X7YQJ05Kw",
    authDomain: "patient-detection-reader.firebaseapp.com",
    databaseURL: "https://patient-detection-reader.firebaseio.com",
    projectId: "patient-detection-reader",
    storageBucket: "patient-detection-reader.appspot.com",
    messagingSenderId: "428871775110"
};

export const firebaseApp = firebase.initializeApp(config);
export const patientRef = firebase.database().ref("patientTest");