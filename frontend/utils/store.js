const store = new Vuex.Store({
  state: {
    auth_token: null,
    role: null,
    loggedIn: false,
    user_id: null,
  },
  mutations: {
    setUser(state) {
      try {
        const user = JSON.parse(localStorage.getItem('user'));  
        if (user && user.token) {
          state.auth_token = user.token;
          state.role = user.role;
          state.loggedIn = true;
          state.user_id = user.id;
          console.log('User found:', user);  
        } else {
          console.warn('No token found in localStorage');
        }
      } catch (error) {
        console.error('Error parsing user from localStorage:', error);
      }
    },
    logout(state) {
      state.auth_token = null;
      state.role = null;
      state.loggedIn = false;
      state.user_id = null;

      localStorage.removeItem('user');
    },
  },
  actions: {},
});

// Run this mutation when the page is reloaded
store.commit('setUser');

export default store;
