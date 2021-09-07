import { Component, OnInit } from '@angular/core';
import employees from "../../assets/employees.json";

@Component({
  selector: 'app-day01',
  templateUrl: './day01.component.html',
  styleUrls: ['./day01.component.scss']
})
export class Day01Component implements OnInit {

  constructor() { }

  ngOnInit(): void {
    console.log(employees);
  }

}
