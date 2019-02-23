import React from 'react'; //You need these two things for anything to work in react
import ReactDOM from 'react-dom'; // they provide the react structure and stuff
import {Router, Route, browserHistory} from 'react-router'; //This is how you make multiple pages, it's kinda dumb.
//For react-router we are using V.3 because V.4 doesn't support browserHistory.
//We might migrate in the future, but for now let's use V.3

import App from './components/app'; //These are the components, 
import SignIn from './components/SignIn'; // you need to import them to the main index for things to work.
import SignUp from './components/SignUp';

ReactDOM.render(
    <Router path="/" history={browserHistory}> 
        <Route path="/app" component={App} /> 
        <Route path="/signin" component={SignIn} />
        <Route path= "/signup" component={SignUp} />
    </Router>, document.getElementById('root')
)