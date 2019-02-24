import React from 'react'; //You need these two things for anything to work in react
import ReactDOM from 'react-dom'; // they provide the react structure and stuff
import {Router, Route, browserHistory} from 'react-router'; //This is how you make multiple pages, it's kinda dumb.
//For react-router we are using V.3 because V.4 doesn't support browserHistory.
//We might migrate in the future, but for now let's use V.3

import {firebaseApp} from './firebase';

import App from './components/app'; //These are the components, 
import SignIn from './components/SignIn'; // you need to import them to the main index for things to work.
import SignUp from './components/SignUp';

//so this is the firebase listener, it returns if a user has logged in or logged out
//the same logic can be applied to singing up / not signing up sooooo
firebaseApp.auth().onAuthStateChanged(user => {
    if (user) {
        console.log('user has signed in or up', user);
    }
    else{
        console.log('user has signed out or still needs to sign up')
    }
})

//this is the router nonsense and allows for $domain.something/{.jsx}
ReactDOM.render(
    <Router path="/" history={browserHistory}> 
        <Route path="/app" component={App} /> 
        <Route path="/signin" component={SignIn} />
        <Route path= "/signup" component={SignUp} />
    </Router>, document.getElementById('root')
)