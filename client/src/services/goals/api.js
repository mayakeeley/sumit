import { ModelAPI } from '@thinknimble/tn-models'

import AxiosClient from '../AxiosClient'

// NOTE: The AxiosClient is congfigured to include '/api' in the baseUrl
const GOALS_ENDPOINT = '/goals/'

export default class GoalAPI extends ModelAPI {
  /**
   * ModelAPI contains methods for list and create (overridden here) and the FILTERS_MAP
   * You may override any of these methods by statically defining them here
   * e.g static FILTERS_MAP={...UserAPI.FILTERS_MAP, <FITERS>}
   *      list({ filters = {}, pagination = {} }){
   *
   * }
   */

  get client() {
    return AxiosClient
  }

  static ENDPOINT = GOALS_ENDPOINT

  static FILTERS_MAP = {
    ...GoalAPI.FILTERS_MAP,
    // Custom Filters
  }
}
