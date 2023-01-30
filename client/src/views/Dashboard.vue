<template>
  <div>
    <h1 class="heading">This is your dashboard</h1>
    <p v-if="loading"></p>
    <div v-else>
      <h2>Goals</h2>
      <div class="border" v-for="goal in goals.list" :key="goal.id">
        <h3>{{ goal.name }} - {{ goal.active ? 'Started' : 'Not Started' }}</h3>
        <p class="mx-2">
          {{
            goal.total.toLocaleString('en-US', {
              style: 'currency',
              currency: goal.currencyRef.code,
            })
          }}{{ goal.goalType == 'PERCENT' ? '%' : '' }}
          {{ goal.goalFormat == 'MONTHLY' ? '/month' : '' }}
        </p>
        <p>{{ goal.endDate ? formatDate(goal.endDate) : 'N/A' }}</p>
        <p>
          {{
            goal.currentBalance.toLocaleString('en-US', {
              style: 'currency',
              currency: goal.currencyRef.code,
            })
          }}
        </p>
        <p>{{ goal.achieved ? 'Y' : 'N' }}</p>
        <p>{{ goal.progress + '%' }}</p>
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

    const formatDate = (date) => {
      const newDate = new Date(date)
      return newDate.toLocaleDateString()
    }
    return {
      goals,
      loading,
      formatDate,
    }
  },
}
</script>
