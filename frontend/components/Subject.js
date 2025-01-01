export default {
  props: ["name", "description", "id"], 
  template: `
    <div class="card h-100 shadow-sm">
      <div class="card-body">
        <h5 class="card-title text-center text-truncate">{{ name }}</h5>
        <p class="card-text text-center">{{ description }}</p>
      </div>
      <div class="card-footer d-flex justify-content-between">
        <button 
          class="btn btn-primary btn-sm"
          @click="onModify"
        >
          Modify
        </button>
        <button 
          class="btn btn-danger btn-sm"
          @click="onDelete"
        >
          Delete
        </button>
        <button 
          class="btn btn-secondary btn-sm"
          @click="onSeeMore"
        >
          See More
        </button>
      </div>
    </div>
  `,
  methods: {
    onModify() {
      console.log(`Modify clicked for ID: ${this.id}`);
      // Add your logic for modifying here
    },
    onDelete() {
      console.log(`Delete clicked for ID: ${this.id}`);
      // Add your logic for deleting here
    },
    onSeeMore() {
      console.log(`See More clicked for ID: ${this.id}`);
    },
  },
};
