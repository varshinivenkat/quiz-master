import Subject from "../components/Subject.js";

    export default {
      template: `
      <div class="container mt-5">
      <div class="row g-4">
        <div 
          v-for="sub in subjects" 
          :key="sub.id" 
          class="col-12 col-md-6 col-lg-4">
          <div class="card shadow-sm h-100">
            <img 
              v-if="sub.image" 
              :src="sub.image" 
              :alt="sub.name" 
              class="card-img-top"
            />
            <div class="card-body d-flex flex-column">
              <h5 class="card-title text-center text-truncate">{{ sub.name }}</h5>
              <p class="card-text text-center flex-grow-1">{{ sub.description }}</p>
            </div>
            <div class="card-footer d-flex justify-content-between">
              <button 
                class="btn btn-primary btn-sm"
                @click="onModify(sub.id)"
              >
                Modify
              </button>
              <button 
                class="btn btn-danger btn-sm"
                @click="onDelete(sub.id)"
              >
                Delete
              </button>
              <button 
                class="btn btn-secondary btn-sm"
                @click="onSeeMore(sub.id)"
              >
                See More
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
      `,
      data() {
        return {
          subjects: [],
        };
      },
      async mounted() {
        try {
          const user = JSON.parse(localStorage.getItem("user"));

          if (user && user.token) {
            const res = await fetch(`${location.origin}/api/subjects`, {
              headers: {
                "Authentication-Token": this.$store.state.auth_token,
              },
            });

            if (res.ok) {
              this.subjects = await res.json();
            } else {
              console.error("Failed to fetch subjects:", res.statusText);
            }
          } else {
            console.error("User is not logged in or no token found");
          }
        } catch (error) {
          console.error("Error during fetch request:", error);
        }
      },
      components: {
        Subject,
      },
    };

