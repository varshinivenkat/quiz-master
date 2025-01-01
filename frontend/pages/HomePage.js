
export default {
  template: `
  <div>
  <div class="d-flex justify-content-center align-items-center vh-100">
    <div class="card text-white bg-primary mb-3" style="max-width: 50rem; opacity: 0.9;">
      <div class="card-body">
        <h4 class="card-title text-center mb-4" style="font-size: 25px; font-weight: bold;">WELCOME TO QUIZ MASTER!</h4>
        <p class="card-text mb-4 text-center">
          Quiz Master is the ultimate platform for testing your knowledge and competing against friends and players around the world. With a wide range of quizzes across various topics, it's the perfect place to challenge your mind, track your progress, and become the Quiz Master!
        </p>

        <h5 class="mb-3 text-center" style="font-size: 20px; font-weight: bold;">Enhance Your Quiz Master Experience</h5>
        <div class="d-flex justify-content-around">
          <div class="card bg-light text-dark mb-3 text-center" style="width: 15rem;">
            <div class="card-body">
              <h6 class="card-title" style="font-size: 18px; font-weight: bold;">Daily Reminders to Keep You On Track</h6>
            </div>
          </div>

          <div class="card bg-light text-dark mb-3 text-center" style="width: 15rem;">
            <div class="card-body">
              <h6 class="card-title" style="font-size: 18px; font-weight: bold;">Personalized Monthly Activity Report</h6>
            </div>
          </div>

          <div class="card bg-light text-dark mb-3" style="width: 15rem;">
            <div class="card-body  text-center">
              <h6 class="card-title" style="font-size: 18px; font-weight: bold;">Export Your Quiz Data as HTML or PDF</h6>
            </div>
          </div>
        </div>

        <div class="text-center">
         <router-link to="/login" class="btn btn-warning text-light" style="font-weight: bold; font-size : 18px">Get Started</router-link>
        </div>
      </div>
    </div>
  </div>
  </div>
  `,
}
