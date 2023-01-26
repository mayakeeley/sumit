<template>
  <div>
    <h1 class="heading">This is your dashboard</h1>
    <p v-if="loading"></p>
    <div v-else>
      <h2>Goals</h2>
      <div v-for="goal in goals.list" :key="goal.id">
        <h3>{{ goal.name }}</h3>
        <p>
          {{ goal.goalType == 'NUMBER' ? goal.currencyRef.symbol : '' }}{{ goal.total
          }}{{ goal.goalType == 'PERCENT' ? '%' : '' }}
          {{ goal.goalFormat == 'MONTHLY' ? '/month' : '' }}
        </p>
        <p>{{ goal.endDate }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import Goal from '@/services/goals'
import { CollectionManager } from '@thinknimble/tn-models'
import { ref, onBeforeMount, computed } from 'vue'
export default {
  name: 'Dashboard',
  setup() {
    const goals = ref(
      CollectionManager.create({
        ModelClass: Goal,
        filters: {
          ordering: 'end_date',
        },
      }),
    )
    const loading = computed(() => goals.value.refreshing)
    onBeforeMount(async () => {
      await goals.value.refresh()
    })
    return {
      goals,
      loading,
    }
  },
}
</script>
