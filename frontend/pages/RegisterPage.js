
export default {
  template: `
    <div class="d-flex justify-content-center align-items-center vh-100" style = "opacity: 0.9;" >
      <div class="card text-white bg-primary mb-3" style="max-width: 70rem; margin-top: 80px; ">
        <div class="card-body">
          <h2 class="card-title text-center mb-4" style="font-size: 40px; font-weight: bold;">REGISTER</h2>
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
          <div class="mb-4">
            <input 
              type="text" 
              placeholder="Name" 
              v-model="name" 
              class="form-control form-control-lg"
              style="font-size: 20px;"
            />
          </div>
          <div class="mb-4">
            <input 
              type="text" 
              placeholder="Qualification" 
              v-model="qualification" 
              class="form-control form-control-lg"
              style="font-size: 20px;"
            />
          </div>
          <div class="mb-4">
            <input 
              type="date" 
              placeholder="Date of Birth" 
              v-model="dob" 
              class="form-control form-control-lg"
              style="font-size: 20px;"
            />
          </div>
          <div class="d-flex justify-content-center">
            <button 
              @click="submitRegister" 
              class="btn btn-warning text-light mb-4"
              style="font-size: 20px; font-weight: bold;"
            >
              Register
            </button>
      </div>
        </div>
      </div>
    </div>
  `,
  data() {
    return {
      email: null,
      password: null,
      name: null,
      qualification: null,
      dob: null,
      errorMessage: null, 
    };
  },
  methods: {
    async submitRegister() {
      try {
        const res = await fetch(location.origin + '/register', {
          method: 'POST',
          body: JSON.stringify({
            email: this.email,
            password: this.password,
            name: this.name,
            qualification: this.qualification,
            dob: this.dob,
          }),
          headers: {
            'Content-Type': 'application/json',
          },
        });

        if (!res.ok) {
          const errorData = await res.json();
          this.errorMessage = errorData.message || 'Registration failed. Please try again.';
          console.error('Registration failed:', errorData);
        } else {
          console.log('User registered successfully');
        }
      } catch (error) {
        this.errorMessage = 'An error occurred. Please try again later.';
        console.error('An unexpected error occurred:', error);
      }
    },
  },
};
