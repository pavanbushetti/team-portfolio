import { Routes } from '@angular/router';
import { Person } from './person/person';

export const routes: Routes = [
  {
    path: 'person/:personId',
    component: Person
  }
];