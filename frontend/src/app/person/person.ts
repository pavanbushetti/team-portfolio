import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-person',
  imports: [CommonModule],
  templateUrl: './person.html',
  styleUrl: './person.css'
})
export class Person {

  person: any = null;

  constructor(
    private http: HttpClient,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {

    const personId =
      this.route.snapshot.paramMap.get('personId');

    this.http.get<any>(
      `http://127.0.0.1:8000/api/person/${personId}`
    ).subscribe({

      next: (result) => {
        this.person = result;
      },

      error: (error) => {
        console.error(error);
      }

    });
  }
}