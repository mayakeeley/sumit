import Model, { fields } from '@thinknimble/tn-models'
import GoalAPI from './api'

export class Category extends Model {
  static id = new fields.IdField({ readOnly: true })
  static name = new fields.CharField()
}

export class Subcategory extends Model {
  static id = new fields.IdField({ readOnly: true })
  static name = new fields.CharField()
  static categoryRef = new fields.ModelField({ ModelClass: Category })
}

export class Currency extends Model {
  static id = new fields.IdField({ readOnly: true })
  static name = new fields.CharField()
  static code = new fields.CharField()
  static symbol = new fields.CharField()
}

export default class Goal extends Model {
  static api = GoalAPI.create(Goal)

  static id = new fields.IdField({ readOnly: true })
  static name = new fields.CharField()
  static datetimeCreated = new fields.CharField()
  static lastUpdated = new fields.CharField()
  static subcategoryRef = new fields.ModelField({ ModelClass: Subcategory })
  static goalType = new fields.CharField()
  static goalFormat = new fields.CharField()
  static startDate = new fields.CharField()
  static endDate = new fields.CharField()
  static total = new fields.IntegerField()
  static currencyRef = new fields.ModelField({ ModelClass: Currency })
}
