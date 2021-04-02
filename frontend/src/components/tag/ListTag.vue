<template lang="html">
    <div class="tags-content-box">
        <div class="button-box">
            <button class="btn btn--1">+</button>
            <button class="btn btn--1">-</button>
        </div>
        <div class="tags-box">
            <b-table class="tag" striped hover :items="tags">
                
            </b-table>

        </div>
    </div>
</template>



<script>
import axios from 'axios'

export default {
    data () {
        return {
            fields: [
                {key: 'title', label: 'Titulo'},
                {key: 'description', label: 'Descripción'},
                {key: 'action', label: 'Acción'}
            ],
            tags: []
        }
    },
    methods: {
        getTags() {
            const path = 'http://localhost:8000/api/tags/'
            axios.get(path).then((response) => {
                this.tags = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    created(){
        this.getTags()
    }
}
</script>

<style lang="css" scoped>
</style>