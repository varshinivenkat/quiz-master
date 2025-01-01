export default {
  template: `
    <div>
    <div class="d-flex justify-content-center align-items-center vh-100" >
    <div class="card text-white bg-primary mb-3" style="max-width: 70rem; opacity: 0.9; ">
      <div class="card-body">
        <h2 class="card-title text-center mb-4" style="font-size: 40px; font-weight: bold;">LOGIN</h2>
        <div v-if="errorMessage" class="alert alert-danger" role="alert">
          {{ errorMessage }}
        </div>
        <div class="mb-4">
          <input 
            type="email" 
            placeholder="Email" 
            v-model="email" 
            class="form-control form-control-lg"
            style="font-size: 20px;"
          />
        </div>
        <div class="mb-4">
          <input 
            type="password" 
            placeholder="Password" 
            v-model="password" 
            class="form-control form-control-lg"
            style="font-size: 20px;"
          />
        </div>
        <div class="d-flex justify-content-center">
        <button 
          @click="submitLogin" 
          class="btn btn-warning text-light mb-4"
          style="font-size: 20px; font-weight: bold;"
        >
          Login
        </button>
      </div>
      
        <div class="text-center">
          <a href="/forgot-password" class="text-white" style="font-size: 18px; text-decoration: underline;">Forgot Password?</a>
        </div>
      </div>
    </div>
  </div>
    </div>
  `,
  data() {
    return {
      email: null,
      password: null,
      errorMessage: null, // To store error message
    };
  },
  methods: {
    async submitLogin() {
      try {
        const res = await fetch(location.origin + '/login', {
          method: 'POST',
          body: JSON.stringify({ email: this.email, password: this.password }),
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (!res.ok) {
          const errorData = await res.json();
          this.errorMessage = errorData.message || 'Login failed. Please try again.';
          console.error('Login failed:', errorData);
        } else {
          console.log('We are logged in');
          const data = await res.json();
          console.log(data);

          localStorage.setItem('user', JSON.stringify(data))
          this.$store.commit('setUser')
          this.$router.push('/admin_dashboard')
        }
      } catch (error) {
        this.errorMessage = 'An error occurred. Please try again later.';
        console.error('An unexpected error occurred:', error);
      }
    },
  },
};
