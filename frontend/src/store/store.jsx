import { createStore } from 'redux'
let INITIAL_STATE = false;

function store(state = INITIAL_STATE, action) {
	if (action.type){
		INITIAL_STATE = !INITIAL_STATE
		console.log(`return ${INITIAL_STATE}`)
		return !INITIAL_STATE
	}  
  
}

export default store;